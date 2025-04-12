"use client"
import { useState } from "react"
import { Copy, Check } from "lucide-react"

export function AccessTokenDisplay({ token }: any) {
  const [copied, setCopied] = useState(false)

  const copyToClipboard = async () => {
    if (!token) return

    try {
      await navigator.clipboard.writeText(token)
      setCopied(true)
      setTimeout(() => setCopied(false), 2000)
    } catch (err) {
      console.error("Failed to copy: ", err)
    }
  }

  return (
    <div className="w-full max-w-2xl">
      <div className="flex justify-between items-center mb-1">
        <span className="text-xs text-muted-foreground">Access Token</span>
        <button
          onClick={copyToClipboard}
          className="flex items-center gap-1 text-xs text-primary hover:text-primary/80 transition-colors"
          aria-label="Copy access token to clipboard"
        >
          {copied ? (
            <>
              <Check size={16} /> Copied!
            </>
          ) : (
            <>
              <Copy size={16} /> Copy
            </>
          )}
        </button>
      </div>
      <div className="relative">
        <pre className="text-xs font-mono p-3 rounded border w-full overflow-x-auto whitespace-pre-wrap break-all">
          {token || "No token available"}
        </pre>
      </div>
    </div>
  )
}
