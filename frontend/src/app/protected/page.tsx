import { createClient } from "@/lib/supabase/server"
import { InfoIcon } from "lucide-react"
import { AccessTokenDisplay } from "./AccessTokenDisplay"
import { api } from "@/lib/api"

interface ProtectedResponse {
  message: string
}

export default async function Home() {
  const supabase = await createClient()

  const {
    data: { user },
  } = await supabase.auth.getUser()

  const session = await supabase.auth.getSession()

  // Make the protected API call
  let protectedData: ProtectedResponse = {
    message: "Failed to fetch protected data",
  }
  try {
    protectedData = await api.get<ProtectedResponse>("/protected")
  } catch (error) {
    console.error("Error fetching protected data:", error)
  }

  if (!user) {
    return <>Not logged in!</>
  }

  return (
    <>
      <h1>The dashboard will go here!</h1>
      <p>API Response: {protectedData.message}</p>
      <div className="flex-1 w-full flex flex-col gap-12">
        <div className="w-full">
          <div className="bg-accent text-sm p-3 px-5 rounded-md text-foreground flex gap-3 items-center">
            <InfoIcon size="16" strokeWidth={2} />
            This is a protected page that you can only see as an authenticated
            user
          </div>
        </div>
        <div className="flex flex-col gap-2 items-start">
          <h2>Your JWT is</h2>
          <AccessTokenDisplay token={session.data.session?.access_token} />

          <h2 className="font-bold text-2xl mb-4">Your user details</h2>
          <pre className="text-xs font-mono p-3 rounded border max-h-32 overflow-auto">
            {JSON.stringify(user, null, 2)}
          </pre>
        </div>
      </div>
    </>
  )
}
