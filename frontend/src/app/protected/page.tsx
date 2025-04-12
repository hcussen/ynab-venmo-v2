import { createClient } from "@/lib/supabase/server"
import { InfoIcon } from "lucide-react"
import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"

type Transaction = {
  id: string
  transaction_date: string
  amount: number
  payee_name: string
  memo: string
  posted_to_ynab: "not_posted" | "posted_success" | "posted_error"
  cleared: boolean
}

export default async function Home() {
  const supabase = await createClient()

  const {
    data: { user },
  } = await supabase.auth.getUser()

  if (!user) {
    return <div>Not logged in</div>
  }

  const { data: transactions, error } = await supabase
    .from("transactions")
    .select("*")
    .eq("profile_id", user.id)
    .order("transaction_date", { ascending: false })

  if (error) {
    console.error("Error fetching transactions:", error)
    return <div>Error loading transactions</div>
  }

  return (
    <>
      <h1 className="text-2xl font-bold">Your Transactions</h1>
      <Table>
        <TableCaption>A list of your transactions.</TableCaption>
        <TableHeader>
          <TableRow>
            <TableHead>Date</TableHead>
            <TableHead>Payee</TableHead>
            <TableHead>Memo</TableHead>
            <TableHead>Status</TableHead>
            <TableHead className="text-right">Amount</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {transactions.map((transaction: Transaction) => (
            <TableRow key={transaction.id}>
              <TableCell className="font-medium">
                {new Date(transaction.transaction_date).toLocaleDateString(
                  "en-US",
                  { month: "short", day: "numeric", year: "numeric" }
                )}
              </TableCell>
              <TableCell>{transaction.payee_name}</TableCell>
              <TableCell>{transaction.memo}</TableCell>
              <TableCell>
                {transaction.posted_to_ynab === "posted_success" ? (
                  <span className="text-green-600">Synced</span>
                ) : transaction.posted_to_ynab === "posted_error" ? (
                  <span className="text-red-600">Error syncing</span>
                ) : (
                  <span className="text-yellow-600">Not synced yet</span>
                )}
              </TableCell>
              <TableCell className="text-right">
                ${(Math.abs(transaction.amount) / 1000).toFixed(2)}
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </>
  )
}
