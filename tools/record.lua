function Table(record)
  record.bodies[1].row_head_columns = 1
  record.colspecs = {
    {"AlignDefault", 0.14}, {"AlignDefault", 0.36},
    {"AlignDefault", 0.37}, {"AlignDefault", 0.13},
  }
  return pandoc.Div(record, pandoc.Attr("", {"record"}))
end
