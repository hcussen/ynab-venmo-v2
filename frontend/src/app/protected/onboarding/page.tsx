"use client"

import { useRouter, useSearchParams } from "next/navigation"
import { useState, Suspense } from "react"
import ConnectYnabStep from "./ConnectYnabStep"
import SetupCompleteStep from "./SetupCompleteStep"
import OAuthCallback from "./OauthCallbackStep"

// Create a separate component for handling search params
function StepRenderer({ completedSteps, completeStep, goToStep }: any) {
  const searchParams = useSearchParams()
  const currentStep = searchParams.get("step") || "connect-ynab"

  // Your switch case for rendering steps
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
      return <SetupCompleteStep />
    default:
      return <div>Unknown step</div>
  }
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
  const currentStepIndex = 1 // Default, will be updated by StepRenderer

  return (
    <div className="onboarding-container">
      <div className="progress-bar">
        <div>
          Step {currentStepIndex} of {totalSteps}
        </div>
      </div>

      <Suspense fallback={<div>Loading...</div>}>
        <StepRenderer
          completedSteps={completedSteps}
          completeStep={completeStep}
          goToStep={goToStep}
        />
      </Suspense>
    </div>
  )
}
