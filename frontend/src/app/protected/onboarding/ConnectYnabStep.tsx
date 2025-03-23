// app/onboarding/steps/ConnectYNABStep.jsx
import { Button } from "@/components/ui/button"
import { getApiUrl } from "@/lib/api"
import Link from "next/link"

export default function ConnectYNABStep() {
  return (
    <div className="step-container">
      <Link
        href={`https://app.ynab.com/oauth/authorize?client_id=${process.env.NEXT_PUBLIC_YNAB_CLIENT_ID}&redirect_uri=${getApiUrl()}/${process.env.NEXT_PUBLIC_YNAB_REDIRECT_URI}&response_type=code`}
      >
        <Button>Connect to YNAB</Button>
      </Link>
    </div>
  )
}
