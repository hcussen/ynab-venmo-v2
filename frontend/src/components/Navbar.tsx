import { metadata } from "@/app/layout"
import Link from "next/link"
import HeaderAuth from "@/components/header-auth"

export const Navbar = () => {
  return (
    <nav className="w-full flex justify-center border-b border-b-foreground/10 h-16">
      <div className="w-full max-w-5xl flex justify-between items-center p-3 px-5 text-sm">
        <div className="flex gap-5 items-center">
          <Link href={"/"} className="font-semibold">
            {metadata.title}
          </Link>
          <Link href="/protected">Overview</Link>
          <Link href="/privacy-policy">Privacy</Link>
          <Link href="/protected/settings">Settings</Link>
        </div>
        <HeaderAuth />
      </div>
    </nav>
  )
}
