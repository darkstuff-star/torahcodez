import { useEffect, useState } from 'react'

import Options from './Options'
import Results from './Results'

type TextInfo = { id: string; label: string }

export type SearchOptions = {
  query_en: string
  directions: string[]
  gridWidth: number
  skipMin: number
  skipMax: number
  layers: number
  codex: string
  reverse: boolean
}

export type SearchResponse = {
  query_he: string
  hits: GridHit[]
  textId: string
}

export type GridHit = {
  dir: string
  skip: number
  start: number
  length: number
  span: [number, number]
  grid: { r: number; c: number; N: number }
  layer: number
}

const DEFAULT_OPTIONS: SearchOptions = {
  query_en: '',
  directions: ['E', 'W', 'N', 'S', 'NE', 'NW', 'SE', 'SW'],
  gridWidth: 50,
  skipMin: 1,
  skipMax: 500,
  layers: 1,
  codex: 'GENESIS_1_5',
  reverse: false,
}

export default function App() {
  const [texts, setTexts] = useState<TextInfo[]>([])
  const [opts, setOpts] = useState<SearchOptions>(DEFAULT_OPTIONS)
  const [res, setRes] = useState<SearchResponse | null>(null)

  useEffect(() => {
    fetch('/texts')
      .then((r) => r.json())
      .then((data) => setTexts(data))
      .catch(() => setTexts([]))
  }, [])

  const onSearch = async () => {
    const response = await fetch('/search', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(opts),
    })
    const json = (await response.json()) as SearchResponse
    setRes(json)
  }

  return (
    <div
      style={{
        display: 'grid',
        gridTemplateColumns: '360px 1fr',
        minHeight: '100vh',
        background: '#0b1220',
        color: '#d7dde8',
      }}
    >
      <Options opts={opts} setOpts={setOpts} onSearch={onSearch} texts={texts} />
      <Results res={res} />
    </div>
  )
}
