import type { GridHit, SearchResponse } from './App'

type Props = {
  res: SearchResponse | null
}

export default function Results({ res }: Props) {
  if (!res) {
    return <div style={{ padding: 16 }} />
  }

  const hits = res.hits || []

  return (
    <div style={{ padding: 16 }}>
      <h3>Query Hebrew: {res.query_he}</h3>
      <table style={{ width: '100%', borderCollapse: 'collapse', marginTop: 12 }}>
        <thead>
          <tr>
            <th>Dir</th>
            <th>Skip</th>
            <th>Start</th>
            <th>Length</th>
            <th>Span</th>
            <th>Row</th>
            <th>Col</th>
            <th>Layer</th>
          </tr>
        </thead>
        <tbody>
          {hits.map((h: GridHit, i: number) => {
            const N = h.grid.N
            const r = Math.floor(h.start / N)
            const c = h.start % N
            return (
              <tr key={i}>
                <td>{h.dir}</td>
                <td>{h.skip}</td>
                <td>{h.start}</td>
                <td>{h.length}</td>
                <td>
                  {h.span[0]}..{h.span[1]}
                </td>
                <td>{r}</td>
                <td>{c}</td>
                <td>{h.layer}</td>
              </tr>
            )
          })}
        </tbody>
      </table>
    </div>
  )
}
