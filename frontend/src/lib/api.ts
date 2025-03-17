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
