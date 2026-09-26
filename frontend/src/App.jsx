import { useState } from 'react'
import ReactMarkdown from 'react-markdown'
import './App.css'

const API_URL = 'http://127.0.0.1:8000/plan-trip'

function App() {
  const [message, setMessage] = useState('')
  const [response, setResponse] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState('')

  const handleSubmit = async (event) => {
    event.preventDefault()

    const userMessage = message.trim()

    if (!userMessage || isLoading) {
      return
    }

    setIsLoading(true)
    setError('')
    setResponse('')

    try {
      const res = await fetch(API_URL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userMessage }),
      })

      if (!res.ok) {
        throw new Error(`Request failed with status ${res.status}`)
      }

      const data = await res.json()
      const aiResponse = data && typeof data.response === 'string' ? data.response : 'No travel plan available yet.'

      setResponse(aiResponse)
    } catch (fetchError) {
      const isNetworkFailure =
        fetchError instanceof TypeError ||
        fetchError?.message?.includes('Failed to fetch') ||
        fetchError?.message?.includes('NetworkError')

      if (isNetworkFailure) {
        setError(
          'Unable to connect to the travel agent. Please make sure the FastAPI server is running. If the browser shows a CORS error, enable CORS in FastAPI.',
        )
      } else {
        setError(
          'The travel agent could not generate a response. Please try again in a moment.',
        )
      }
    } finally {
      setIsLoading(false)
    }
  }

  const handleKeyDown = (event) => {
    if (event.key === 'Enter' && !event.shiftKey) {
      event.preventDefault()
      handleSubmit(event)
    }
  }

  return (
    <div className="min-h-screen bg-slate-950 text-slate-50">
      <div className="mx-auto max-w-5xl px-4 py-8 sm:px-6 lg:px-8">
        <header className="flex items-center justify-between rounded-full border border-white/10 bg-white/5 px-4 py-3 shadow-soft backdrop-blur-sm sm:px-6">
          <div className="flex items-center gap-3">
            <div className="flex h-10 w-10 items-center justify-center rounded-full bg-gradient-to-br from-cyan-400 to-blue-600 text-lg shadow-lg shadow-cyan-500/20">
              ✈️
            </div>
            <div>
              <p className="text-lg font-semibold tracking-tight text-white">Travel AI</p>
              <p className="text-xs text-slate-300">Plan your trip with AI</p>
            </div>
          </div>
        </header>

        <main className="mt-10">
          <div className="rounded-[2rem] border border-white/10 bg-white/5 p-5 shadow-soft backdrop-blur-sm sm:p-8 lg:p-10">
            <div className="max-w-3xl">
              <p className="mb-3 inline-flex rounded-full border border-cyan-400/30 bg-cyan-500/10 px-3 py-1 text-xs font-medium uppercase tracking-[0.2em] text-cyan-200">
                AI trip planner
              </p>
              <h1 className="text-4xl font-bold tracking-tight text-white sm:text-5xl">
                Where do you want to go?
              </h1>
              <p className="mt-4 max-w-2xl text-base text-slate-300 sm:text-lg">
                Ask about flights, hotels, weather and places to visit.
              </p>
            </div>

            <form onSubmit={handleSubmit} className="mt-8">
              <label htmlFor="travel-query" className="sr-only">
                Travel query
              </label>
              <textarea
                id="travel-query"
                value={message}
                onChange={(event) => setMessage(event.target.value)}
                onKeyDown={handleKeyDown}
                placeholder="e.g. Plan a 3-day trip to Goa from Delhi..."
                rows={6}
                disabled={isLoading}
                className="w-full resize-none rounded-3xl border border-white/10 bg-slate-900/80 px-5 py-4 text-base text-white placeholder:text-slate-400 focus:border-cyan-400 focus:outline-none focus:ring-2 focus:ring-cyan-500/20 disabled:cursor-not-allowed disabled:opacity-70"
              />

              <div className="mt-4 flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
                <p className="text-sm text-slate-400">
                  Press Enter to send • Shift + Enter for a new line
                </p>

                <button
                  type="submit"
                  disabled={isLoading || !message.trim()}
                  className="inline-flex items-center justify-center rounded-full bg-gradient-to-r from-cyan-400 to-blue-500 px-6 py-3 text-sm font-semibold text-slate-950 shadow-lg shadow-cyan-500/30 transition hover:brightness-110 disabled:cursor-not-allowed disabled:opacity-60"
                >
                  {isLoading ? 'Planning your trip...' : 'Plan Trip'}
                </button>
              </div>
            </form>

            {isLoading && (
              <div className="mt-6 flex items-center gap-3 rounded-2xl border border-cyan-400/20 bg-cyan-500/10 px-4 py-3 text-sm text-cyan-100">
                <span className="h-2.5 w-2.5 animate-pulse rounded-full bg-cyan-300" aria-hidden="true" />
                Planning your trip...
              </div>
            )}

            {error && (
              <div
                role="alert"
                className="mt-6 rounded-2xl border border-rose-400/30 bg-rose-500/10 px-4 py-3 text-sm text-rose-100"
              >
                {error}
              </div>
            )}

            <section className="mt-8 rounded-[1.75rem] border border-white/10 bg-slate-900/70 p-5 sm:p-6">
              <div className="flex items-center justify-between gap-3">
                <h2 className="text-lg font-semibold text-white">Travel response</h2>
                <span className="rounded-full border border-emerald-400/20 bg-emerald-500/10 px-2.5 py-1 text-[10px] font-medium uppercase tracking-[0.2em] text-emerald-200">
                  AI
                </span>
              </div>

              <div className="response-box mt-4 min-h-[180px] text-base leading-7 text-slate-200">
                {response ? (
                  <div className="markdown-content">
                    <ReactMarkdown>{response}</ReactMarkdown>
                  </div>
                ) : (
                  <p className="text-slate-400">Your itinerary and travel insights will appear here.</p>
                )}
              </div>
            </section>
          </div>
        </main>
      </div>
    </div>
  )
}

export default App
