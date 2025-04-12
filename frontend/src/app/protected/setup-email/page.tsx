import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Alert, AlertDescription } from '@/components/ui/alert'
import { CheckCircle2 } from 'lucide-react'

export default function SetupEmailPage() {
  return (
    <div className="container mx-auto py-8 max-w-2xl">
      <Card>
        <CardHeader>
          <CardTitle>Setup Email Forwarding</CardTitle>
          <CardDescription>
            Follow these steps to forward your Venmo transaction emails
          </CardDescription>
        </CardHeader>
        <CardContent className="space-y-6">
          <div className="space-y-4">
            <h3 className="text-lg font-semibold">Steps to Setup:</h3>
            <ol className="list-decimal list-inside space-y-3">
              <li>Open your email client where you receive Venmo notifications</li>
              <li>Create a new email filter or forwarding rule</li>
              <li>Set the following criteria:
                <ul className="list-disc list-inside ml-6 mt-2 space-y-2">
                  <li>From address: <code>venmo@venmo.com</code></li>
                  <li>Forward to: <code>parse@venmoforynab.com</code></li>
                </ul>
              </li>
            </ol>
          </div>

          <Alert>
            <CheckCircle2 className="h-4 w-4" />
            <AlertDescription>
              Once setup, all future Venmo transaction emails will be automatically processed and synced to your YNAB account.
            </AlertDescription>
          </Alert>

          <div className="bg-gray-50 p-4 rounded-lg">
            <h4 className="font-medium mb-2">Common Email Client Instructions:</h4>
            <ul className="list-disc list-inside space-y-2">
              <li><strong>Gmail:</strong> Settings → Filters and Blocked Addresses → Create New Filter</li>
              <li><strong>Outlook:</strong> Settings → Rules → Add New Rule</li>
              <li><strong>Apple Mail:</strong> Mail → Settings → Rules → Add Rule</li>
            </ul>
          </div>
        </CardContent>
      </Card>
    </div>
  )
}
