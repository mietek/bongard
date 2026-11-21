function Table(record)
  record.colspecs = {
    {"AlignDefault", 0.67}, {"AlignDefault", 0.33},
  }
  return pandoc.Div(record, pandoc.Attr("", {"record"}))
end
