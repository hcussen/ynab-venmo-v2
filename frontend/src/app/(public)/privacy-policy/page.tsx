import React from "react"

export default function PrivacyPolicy() {
  return (
    <div className="container mx-auto px-4 py-8 max-w-3xl">
      <h1 className="text-3xl font-bold mb-6">Privacy Policy</h1>

      <section className="mb-8">
        <h2 className="text-2xl font-semibold mb-4">
          Data Collection and Storage
        </h2>
        <p className="mb-4">
          We do not store any YNAB data other than the name of your budget so
          that we can send Venmo transactions to it. Any data collected via your
          Venmo notifications is stored in our database and can be deleted by
          clicking the button on your dashboard at any time.
        </p>
      </section>

      <section className="mb-8">
        <h2 className="text-2xl font-semibold mb-4">
          Third-Party Data Sharing
        </h2>
        <p className="mb-4">
          We guarantee that any data obtained through the YNAB API will not be
          knowingly shared with or passed to any third parties. Your financial
          data privacy is our top priority, and we maintain strict controls to
          ensure your information remains secure and confidential.
        </p>
      </section>

      <section className="mb-8">
        <h2 className="text-2xl font-semibold mb-4">Security Measures</h2>
        <p className="mb-4">
          We implement industry-standard security measures to protect your data.
          All communication with the YNAB API is conducted over secure,
          encrypted connections. We follow best practices for data security and
          regularly update our security protocols to maintain the highest
          standards of data protection.
        </p>
      </section>

      <section className="mb-8">
        <h2 className="text-2xl font-semibold mb-4">Affiliate Disclosure</h2>
        <div className="p-4 bg-muted rounded-lg border">
          <p className="text-sm text-muted-foreground">
            We are not affiliated, associated, or in any way officially
            connected with YNAB, or any of its subsidiaries or its affiliates.
            The official YNAB website can be found at
            <a
              href="https://www.ynab.com"
              className="text-primary hover:underline ml-1"
            >
              https://www.ynab.com
            </a>
            . The names YNAB and You Need A Budget as well as related names,
            marks, emblems and images are registered trademarks of YNAB.
          </p>
        </div>
      </section>
    </div>
  )
}
