import { createClient } from "@/lib/supabase/server"
import { AccessTokenDisplay } from "./AccessTokenDisplay"
import { api } from "@/lib/api"
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert"
import { Info } from "lucide-react"

interface ProtectedResponse {
  message: string
}

export default async function TokenPage() {
  const supabase = await createClient()

  const {
    data: { user },
  } = await supabase.auth.getUser()

  const session = await supabase.auth.getSession()
  const accessToken = session.data.session?.access_token ?? ""

  // Make the protected API call
  let protectedData: ProtectedResponse = {
    message: "Failed to fetch protected data",
  }
  try {
    protectedData = await api.get<ProtectedResponse>("/protected")
  } catch (error) {
    console.error("Error fetching protected data:", error)
  }

  return (
    <div className="p-4">
      <Alert>
        <Info className="h-4 w-4" />
        <AlertTitle>Heads up!</AlertTitle>
        <AlertDescription>
          This is a protected page only logged-in users can see
        </AlertDescription>
      </Alert>

      <p>API Response: {protectedData.message}</p>
      <h2 className="text-xl font-bold mb-4">Your JWT is</h2>
      <AccessTokenDisplay token={accessToken} />
      <div className="flex flex-col gap-2 items-start">
        <h2 className="font-bold text-2xl mb-4">Your user details</h2>
        <pre className="text-xs font-mono p-3 rounded border max-h-32 overflow-auto">
          {JSON.stringify(user, null, 2)}
        </pre>
      </div>
    </div>
  )
}
