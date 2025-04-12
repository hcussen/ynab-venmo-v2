"use client"

import { useRouter, useSearchParams } from "next/navigation"
import { Suspense, useState } from "react"
import ConnectYnabStep from "./ConnectYnabStep"
import OAuthCallback from "./OauthCallbackStep"
import YnabConnected from "./YnabConnected"

// Create a separate component for handling search params
function StepRenderer({
  completedSteps,
  completeStep,
  goToStep,
  totalSteps,
}: {
  completedSteps: Record<string, boolean>
  completeStep: (step: string) => void
  goToStep: (step: string) => void
  totalSteps: number
}) {
  const searchParams = useSearchParams()
  const currentStep = searchParams.get("step") || "connect-ynab"
  const stepNums = {
    "connect-ynab": 1,
    "oauth-callback": 2,
    "setup-complete": 3,
  }

  function render() {
    switch (currentStep) {
      case "connect-ynab":
        return <ConnectYnabStep />
      case "oauth-callback":
        return (
          <OAuthCallback
            onComplete={() => {
              completeStep("oauth-callback")
              goToStep("setup-complete")
            }}
          />
        )
      case "setup-complete":
        return <YnabConnected />
      default:
        return <div>Unknown step</div>
    }
  }

  // Your switch case for rendering steps
  return (
    <>
      <div className="progress-bar">
        <div>
          {/* @ts-ignore */}
          Step {stepNums[currentStep]} of {totalSteps}
        </div>
      </div>
      {render()}
    </>
  )
}

export default function OnboardingPage() {
  const router = useRouter()

  // Track completed steps
  const [completedSteps, setCompletedSteps] = useState({
    "connect-ynab": false,
    "oauth-callback": false,
    "setup-complete": false,
  })

  // Navigation functions
  const goToStep = (step: any) => {
    const url = new URL(window.location.href)
    url.searchParams.set("step", step)
    router.push(`/protected/onboarding?${url.searchParams.toString()}`)
  }

  const completeStep = (step: any) => {
    setCompletedSteps({
      ...completedSteps,
      [step]: true,
    })
  }

  // Calculate progress
  const totalSteps = Object.keys(completedSteps).length

  return (
    <div className="onboarding-container">
      <Suspense fallback={<div>Loading...</div>}>
        <StepRenderer
          completedSteps={completedSteps}
          completeStep={completeStep}
          goToStep={goToStep}
          totalSteps={totalSteps}
        />
      </Suspense>
    </div>
  )
}
