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
      <div className="flex gap-2">
        <Button
          asChild
          size="sm"
          variant={"outline"}
          disabled
          className="opacity-75 cursor-none pointer-events-none"
        >
          <Link href="/sign-in">Sign in</Link>
        </Button>
        <Button
          asChild
          size="sm"
          variant={"default"}
          disabled
          className="opacity-75 cursor-none pointer-events-none"
        >
          <Link href="/sign-up">Sign up</Link>
        </Button>
      </div>
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
