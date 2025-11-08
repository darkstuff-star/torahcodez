import { ChangeEvent, Dispatch, SetStateAction } from 'react'

import type { SearchOptions } from './App'

type Props = {
  opts: SearchOptions
  setOpts: Dispatch<SetStateAction<SearchOptions>>
  onSearch: () => void
  texts: { id: string; label: string }[]
}

export default function Options({ opts, setOpts, onSearch, texts }: Props) {
  const handleNumberChange = (key: string) => (event: ChangeEvent<HTMLInputElement>) => {
    setOpts({ ...opts, [key]: Number(event.target.value) })
  }

  return (
    <div style={{ padding: 16, borderRight: '1px solid #1f2a44' }}>
      <h2 style={{ marginTop: 0 }}>Torah Codes</h2>

      <label htmlFor="query">English query</label>
      <input
        id="query"
        value={opts.query_en}
        onChange={(e) => setOpts({ ...opts, query_en: e.target.value })}
        style={{ width: '100%', marginBottom: 12 }}
      />

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 8 }}>
        <div>
          <label htmlFor="skipMin">Skip min</label>
          <input
            id="skipMin"
            type="number"
            value={opts.skipMin}
            onChange={handleNumberChange('skipMin')}
            style={{ width: '100%' }}
          />
        </div>
        <div>
          <label htmlFor="skipMax">Skip max</label>
          <input
            id="skipMax"
            type="number"
            value={opts.skipMax}
            onChange={handleNumberChange('skipMax')}
            style={{ width: '100%' }}
          />
        </div>
        <div>
          <label htmlFor="gridWidth">Grid width</label>
          <input
            id="gridWidth"
            type="number"
            value={opts.gridWidth}
            onChange={handleNumberChange('gridWidth')}
            style={{ width: '100%' }}
          />
        </div>
        <div>
          <label htmlFor="layers">Layers</label>
          <input
            id="layers"
            type="number"
            value={opts.layers}
            onChange={handleNumberChange('layers')}
            style={{ width: '100%' }}
          />
        </div>
      </div>

      <label style={{ marginTop: 12, display: 'block' }} htmlFor="codex">
        Text
      </label>
      <select
        id="codex"
        value={opts.codex}
        onChange={(e) => setOpts({ ...opts, codex: e.target.value })}
        style={{ width: '100%', marginBottom: 12 }}
      >
        {texts.map((t) => (
          <option key={t.id} value={t.id}>
            {t.label}
          </option>
        ))}
      </select>

      <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 12 }}>
        <input
          id="rev"
          type="checkbox"
          checked={opts.reverse}
          onChange={(e) => setOpts({ ...opts, reverse: e.target.checked })}
        />
        <label htmlFor="rev">Search reversed</label>
      </div>

      <button
        onClick={onSearch}
        style={{
          width: '100%',
          padding: 10,
          background: '#3867ff',
          color: 'white',
          border: 0,
          borderRadius: 8,
          cursor: 'pointer',
        }}
      >
        Search
      </button>
    </div>
  )
}
