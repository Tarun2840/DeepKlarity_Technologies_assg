export default function HistoryTable({ history, onSelect }) {
  return (
    <div>
      <table border="1" cellPadding="8" cellSpacing="0" style={{width: "100%"}}>
        <thead>
          <tr>
            <th>ID</th>
            <th>Title</th>
            <th>URL</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {history.map((item) => (
            <tr key={item.id}>
              <td>{item.id}</td>
              <td>{item.title}</td>
              <td><a href={item.url} target="_blank">{item.url}</a></td>
              <td>
                <button onClick={() => onSelect(item)}>View</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
