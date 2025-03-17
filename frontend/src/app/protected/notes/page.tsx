// src/app/planets/page.tsx
import { createClient } from "@/lib/supabase/server"
import { fetchPlanets } from "./actions"

export default async function Page() {
  // Fetch data from Supabase
  const supabase = await createClient()
  const { data: notes } = await supabase.from("planets").select()

  // Fetch planets data from our API
  let planets
  let error

  try {
    planets = await fetchPlanets()
  } catch (e) {
    error = e instanceof Error ? e.message : "Failed to fetch planets"
  }

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Data from Supabase:</h1>
      <pre className="bg-gray-100 p-4 rounded mb-8 overflow-auto">
        {JSON.stringify(notes, null, 2)}
      </pre>

      <h1 className="text-2xl font-bold mb-4">Planets from API:</h1>
      {error ? (
        <div className="text-red-500">Error: {error}</div>
      ) : (
        <pre className="bg-gray-100 p-4 rounded overflow-auto">
          {JSON.stringify(planets, null, 2)}
        </pre>
      )}
    </div>
  )
}
