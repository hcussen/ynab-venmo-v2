// app/oauth-callback/page.js

"use client" // Important! Mark as a Client Component

import { useEffect, useState, Suspense } from "react"
import { useSearchParams, useRouter } from "next/navigation"
import { createClient } from "@/lib/supabase/client"
import { getApiUrl } from "@/lib/urls"

export default function OAuthCallback({ onComplete }: any) {
  const searchParams = useSearchParams()
  const router = useRouter()
  const [user, setUser] = useState<any>()
  const [token, setToken] = useState<string>()

  const [status, setStatus] = useState("Processing...")

  // Get the code from search parameters
  const code = searchParams.get("code")

  useEffect(() => {
    async function fetchUser() {
      const supabase = createClient()
      const {
        data: { user },
      } = await supabase.auth.getUser()
      const session = await supabase.auth.getSession()
      const token = session.data.session?.access_token
      return { user, token }
    }

    const loadUser = async () => {
      const result = await fetchUser()
      setUser(result.user ?? "")
      setToken(result.token ?? "")
    }

    loadUser()
  }, [])

  useEffect(() => {
    console.log(user)
  }, [user])

  useEffect(() => {
    // Only run once we have both the code and user data
    if (code && user && token) {
      const processOAuth = async () => {
        try {
          setStatus("Sending data to backend...")

          // Send the code and user ID to your FastAPI backend
          const response = await fetch(`${getApiUrl()}/oauth/callback`, {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
              Authorization: `Bearer ${token}`,
            },
            body: JSON.stringify({
              code: code,
            }),
          })

          if (!response.ok) {
            throw new Error(`Backend returned ${response.status}`)
          }

          const data = await response.json()

          if (data.success) {
            setStatus("OAuth completed successfully!")
            onComplete()
          }

          if (data.error) {
            setStatus(`Error: ${data.message}`)
          }
        } catch (error: any) {
          console.error("Error completing OAuth flow:", error)
          setStatus(`Error: ${error.message}`)
        }
      }

      processOAuth()
    } else if (!user) {
      // Handle case where user isn't authenticated
      setStatus("User not authenticated. Redirecting to login...")
      //   router.push("/login")
    }
  }, [code, user, token, router]) // Dependencies for the effect

  // If we don't have a code, something went wrong with the OAuth redirect
  if (!code) {
    return <div>Error: No authorization code received</div>
  }

  // Show loading state until we're done
  return (
    <Suspense>
      <div className="flex flex-col items-center justify-center min-h-screen p-4">
        <h1 className="text-2xl font-bold mb-4">Completing Authorization</h1>
        <p className="text-lg">{status}</p>
        {/* You could add a spinner here */}
      </div>
    </Suspense>
  )
}
