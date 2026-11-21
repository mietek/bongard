function Table(record)
  record.bodies[1].row_head_columns = 1
  record.colspecs = record.colspecs:map(function(column) return {column[1]} end)
  return pandoc.Div(record, pandoc.Attr("", {"record"}))
end
