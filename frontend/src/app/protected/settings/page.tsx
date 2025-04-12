"use client"
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Trash2 } from "lucide-react"

export default function SettingsPage() {
  return (
    <div className="p-6 max-w-4xl mx-auto">
      <h1 className="text-2xl font-bold mb-8">Settings</h1>

      <div className="space-y-6">
        {/* Last Sync Information */}
        <Card>
          <CardHeader>
            <CardTitle>Last Sync</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-gray-600">
              Last synchronized:{" "}
              <span className="font-medium">April 12, 2025 4:40 PM</span>
            </p>
          </CardContent>
        </Card>

        {/* Current Budget */}
        <Card>
          <CardHeader>
            <CardTitle>Current Budget</CardTitle>
            <CardDescription>
              Your active YNAB budget information
            </CardDescription>
          </CardHeader>
          <CardContent>
            <p className="text-gray-600">
              Active budget:{" "}
              <span className="font-medium">Personal Budget 2025</span>
            </p>
          </CardContent>
        </Card>

        {/* Danger Zone */}
        <Card className="border-red-200">
          <CardHeader>
            <CardTitle className="text-red-600">
              Delete All Transactions
            </CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-gray-600 mb-4">
              Warning: This action cannot be undone. This will permanently
              delete all transactions from our database. It will not affect any
              transactions in YNAB.
            </p>
            <button
              className="bg-red-600 text-white px-4 py-2 rounded hover:bg-red-700 
                         transition-colors duration-200 flex items-center gap-2"
              onClick={() => {
                if (
                  confirm(
                    "Are you sure you want to delete all transactions? This action cannot be undone."
                  )
                ) {
                  // Delete functionality will be implemented here
                  console.log("Deleting transactions...")
                }
              }}
            >
              <Trash2 className="h-5 w-5" />
              Delete All Transactions
            </button>
          </CardContent>
        </Card>

        <Card className="border-red-200">
          <CardHeader>
            <CardTitle className="text-red-600">Delete my account</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-gray-600 mb-4">
              Warning: This action cannot be undone. This will permanently
              delete your account and all associated data. It will not affect
              any transactions in YNAB.
            </p>
            <button
              className="bg-red-600 text-white px-4 py-2 rounded hover:bg-red-700 
                         transition-colors duration-200 flex items-center gap-2"
              onClick={() => {
                if (
                  confirm(
                    "Are you sure you want to delete your account? This action cannot be undone."
                  )
                ) {
                  // Delete functionality will be implemented here
                  console.log("Deleting account...")
                }
              }}
            >
              <Trash2 className="h-5 w-5" />
              Delete My Account
            </button>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}
