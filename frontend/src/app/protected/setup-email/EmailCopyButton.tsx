"use client"

import { Button } from "@/components/ui/button"
import { Copy, Check } from "lucide-react"
import { useState } from "react"

interface EmailCopyButtonProps {
  emailSlug: string
}

export function EmailCopyButton({ emailSlug }: EmailCopyButtonProps) {
  const [copied, setCopied] = useState(false)

  const copyEmail = async () => {
    const email = `${emailSlug}@parse.venmoforynab.com`
    await navigator.clipboard.writeText(email)
    setCopied(true)
    setTimeout(() => setCopied(false), 2000)
  }

  return (
    <Button
      variant="ghost"
      size="sm"
      onClick={copyEmail}
      className="h-8 px-2 ml-2"
    >
      {copied ? (
        <Check className="h-4 w-4" />
      ) : (
        <Copy className="h-4 w-4" />
      )}
      <span className="sr-only">Copy email address</span>
    </Button>
  )
}
