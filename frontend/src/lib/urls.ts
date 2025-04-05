/**
 * Returns the appropriate API URL based on the current environment
 * @returns string - The base API URL
 */
export function getApiUrl(): string {
  const isDevelopment = process.env.NODE_ENV !== "production"
  return isDevelopment
    ? "http://localhost:8000"
    : (process.env.NEXT_PUBLIC_API_URL ?? "")
}

export function getFrontendUrl(): string {
  const isDevelopment = process.env.NODE_ENV !== "production"
  return isDevelopment
    ? "http://localhost:3000"
    : (process.env.VERCEL_PROJECT_PRODUCTION_URL ?? "")
}
