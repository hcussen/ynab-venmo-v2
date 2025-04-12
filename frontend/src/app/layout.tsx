import HeaderAuth from "@/components/header-auth"
import { ThemeSwitcher } from "@/components/theme-switcher"
import { ThemeProvider } from "next-themes"
import { Geist } from "next/font/google"
import Link from "next/link"
import "./globals.css"
import { Navbar } from "@/components/Navbar"

const defaultUrl = process.env.VERCEL_URL
  ? `https://${process.env.VERCEL_URL}`
  : "http://localhost:3000"

export const metadata = {
  metadataBase: new URL(defaultUrl),
  title: "YNAB-Venmo integration",
  description: "Automatically sync Venmo transactions to YNAB.",
}

const geistSans = Geist({
  display: "swap",
  subsets: ["latin"],
})

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <html lang="en" className={geistSans.className} suppressHydrationWarning>
      <body className="bg-background text-foreground">
        <ThemeProvider
          attribute="class"
          defaultTheme="system"
          enableSystem
          disableTransitionOnChange
        >
          <main className="min-h-screen flex flex-col items-center">
            <div className="flex-1 w-full flex flex-col gap-20 items-center">
              <Navbar />
              <div className="flex flex-col max-w-5xl p-5">{children}</div>

              <footer className="w-full flex items-center justify-center border-t mx-auto text-center text-xs gap-8 py-16">
                <Link
                  href="/privacy-policy"
                  className="text-muted-foreground hover:text-foreground transition-colors"
                >
                  Privacy Policy
                </Link>
                <ThemeSwitcher />
              </footer>
            </div>
          </main>
        </ThemeProvider>
      </body>
    </html>
  )
}
