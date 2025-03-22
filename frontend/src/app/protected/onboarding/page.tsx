import { Button } from "@/components/ui/button"
import Link from "next/link"

export default function Onboarding() {
  return (
    <>
      <h1>This is where onboarding / email setup will go</h1>
      <Link
        href={`https://app.ynab.com/oauth/authorize?client_id=${process.env.YNAB_CLIENT_ID}&redirect_uri=${process.env.YNAB_REDIRECT_URI}&response_type=code`}
      >
        <Button>Connect to YNAB</Button>
      </Link>
    </>
  )
}
