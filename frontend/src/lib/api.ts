import { createClient } from "@/lib/supabase/server"
import { getApiUrl } from "./urls"

type RequestMethod = "GET" | "POST" | "PUT" | "DELETE"

interface RequestOptions {
  method?: RequestMethod
  body?: any
  headers?: Record<string, string>
}

class ApiClient {
  private static instance: ApiClient
  private baseUrl: string

  private constructor() {
    this.baseUrl = getApiUrl()
  }

  public static getInstance(): ApiClient {
    if (!ApiClient.instance) {
      ApiClient.instance = new ApiClient()
    }
    return ApiClient.instance
  }

  private async getAuthToken(): Promise<string | null> {
    const supabase = await createClient()
    const session = await supabase.auth.getSession()
    return session.data.session?.access_token || null
  }

  private async request<T>(
    endpoint: string,
    options: RequestOptions = {}
  ): Promise<T> {
    const token = await this.getAuthToken()
    console.log("API Request Token:", token ? "Present" : "Missing")

    const headers: Record<string, string> = {
      "Content-Type": "application/json",
      ...options.headers,
    }

    if (token) {
      headers["Authorization"] = `Bearer ${token}`
      console.log("Added Authorization header")
    } else {
      console.log("No token available for request")
    }

    const response = await fetch(`${this.baseUrl}${endpoint}`, {
      method: options.method || "GET",
      headers,
      body: options.body ? JSON.stringify(options.body) : undefined,
    })

    if (!response.ok) {
      throw new Error(`API error: ${response.status} ${response.statusText}`)
    }

    return response.json()
  }

  async get<T>(endpoint: string, headers?: Record<string, string>): Promise<T> {
    return this.request<T>(endpoint, { headers })
  }

  async post<T>(
    endpoint: string,
    body: any,
    headers?: Record<string, string>
  ): Promise<T> {
    return this.request<T>(endpoint, { method: "POST", body, headers })
  }

  async put<T>(
    endpoint: string,
    body: any,
    headers?: Record<string, string>
  ): Promise<T> {
    return this.request<T>(endpoint, { method: "PUT", body, headers })
  }

  async delete<T>(
    endpoint: string,
    headers?: Record<string, string>
  ): Promise<T> {
    return this.request<T>(endpoint, { method: "DELETE", headers })
  }
}

// Export the singleton instance getter
export const api = ApiClient.getInstance()
