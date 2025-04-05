// src/app/actions.ts
"use server"

import { getApiUrl } from "@/lib/urls"

/**
 * Fetches planets data from the API
 * @returns Promise with the planets data
 */
export async function fetchPlanets() {
  try {
    const apiUrl = getApiUrl()
    const response = await fetch(`${apiUrl}/planets`, {
      headers: {
        "Content-Type": "application/json",
      },
      cache: "no-store", // Don't cache the response
    })

    if (!response.ok) {
      throw new Error(`API error: ${response.status}`)
    }

    return await response.json()
  } catch (error) {
    console.error("Error fetching planets:", error)
    throw error
  }
}
