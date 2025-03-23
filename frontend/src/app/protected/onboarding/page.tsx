// app/onboarding/page.jsx
"use client"

import { useRouter, useSearchParams } from "next/navigation"
import { useState, useEffect } from "react"
import ConnectYnabStep from "./ConnectYnabStep"
import SetupCompleteStep from "./SetupCompleteStep"
import OAuthCallback from "./OauthCallbackStep"

export default function OnboardingPage() {
  const router = useRouter()
  const searchParams = useSearchParams()
  const currentStep = searchParams.get("step") || "connect-ynab" // Default step

  // Track completed steps
  const [completedSteps, setCompletedSteps] = useState({
    "connect-ynab": false,
    "oauth-callback": false,
    "setup-complete": false,
  })

  useEffect(() => {
    console.log(completedSteps)
  }, [completedSteps])

  // Navigation functions
  const goToStep = (step) => {
    // Create new URL with updated query params
    const params = new URLSearchParams(searchParams)
    params.set("step", step)
    router.push(`/protected/onboarding?${params.toString()}`)
  }

  const completeStep = (step) => {
    setCompletedSteps({
      ...completedSteps,
      [step]: true,
    })
  }

  // Render the current step
  const renderStep = () => {
    switch (currentStep) {
      case "connect-ynab":
        // Guard against direct URL access
        return (
          <ConnectYnabStep
            onComplete={() => {
              completeStep("connect-ynab")
              goToStep("oauth-callback")
            }}
          />
        )
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
        // Guard against direct URL access
        // if (!completedSteps["connect-ynab"]) {
        //   goToStep("connect-ynab")
        //   return <div>Redirecting...</div>
        // }
        return <SetupCompleteStep />
      default:
        return <div>Unknown step</div>
    }
  }

  // Display progress indicator
  const totalSteps = Object.keys(completedSteps).length
  const currentStepIndex = Object.keys(completedSteps).indexOf(currentStep) + 1

  return (
    <div className="onboarding-container">
      <div className="progress-bar">
        <div>
          Step {currentStepIndex} of {totalSteps}
        </div>
        <div className="step-indicators">
          {Object.keys(completedSteps).map((step, index) => (
            <div
              key={step}
              className={`step-indicator ${
                currentStep === step ? "active" : ""
              } ${completedSteps[step] ? "completed" : ""}`}
            />
          ))}
        </div>
      </div>

      {renderStep()}
    </div>
  )
}
