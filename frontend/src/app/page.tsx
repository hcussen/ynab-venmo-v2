import AuthAware from "@/components/AuthAware"
import { Button } from "@/components/ui/button"
import Link from "next/link"

export default async function Home() {
  const renderSignedIn = () => {
    return (
      <Link href="/protected">
        <Button>Go to dashboard</Button>
      </Link>
    )
  }
  const renderSignedOut = () => {
    return (
      <Link href="/sign-up">
        <Button>Sign Up</Button>
      </Link>
    )
  }
  return (
    <>
      <h1>Welcome to YNAB-Venmo integration!</h1>
      <AuthAware
        renderSignedIn={renderSignedIn}
        renderSignedOut={renderSignedOut}
      />
    </>
  )
}
