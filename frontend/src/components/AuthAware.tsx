import { getUserServer } from "@/lib/auth"

interface AuthAwareProps {
  renderSignedIn: () => React.ReactNode
  renderSignedOut: () => React.ReactNode
}

export default async function AuthAware({
  renderSignedIn,
  renderSignedOut,
}: AuthAwareProps) {
  const user = await getUserServer()
  return user ? renderSignedIn() : renderSignedOut()
}
