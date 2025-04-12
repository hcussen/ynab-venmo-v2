import { createClient as createClientServer } from "@/lib/supabase/server"
import { createClient as createClientClient } from "@/lib/supabase/client"
import { User } from "@supabase/supabase-js"

export async function getUserServer(): Promise<User | null> {
  const supabase = await createClientServer()

  const {
    data: { user },
  } = await supabase.auth.getUser()

  return user ?? null
}

export async function getUserClient(): Promise<User | null> {
  const supabase = await createClientClient()

  const {
    data: { user },
  } = await supabase.auth.getUser()

  return user ?? null
}
