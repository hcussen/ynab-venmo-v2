import Link from "next/link"
import { Button } from "@/components/ui/button"
export default function YnabConnected() {
  return (
    <>
      <h1>Sucessfully connected YNAB!</h1>
      <Link href="/protected/setup-email">
        <Button>Go to email setup</Button>
      </Link>
    </>
  )
}
