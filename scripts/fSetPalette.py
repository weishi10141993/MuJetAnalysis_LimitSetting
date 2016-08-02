def fSetPalette(name="palette", ncontours=999):

  from array import array
  from ROOT import TColor, gStyle

  """Set a color palette from a given RGB list
  stops, red, green and blue should all be lists of the same length
  see set_decent_colors for an example"""

  if name == "gray" or name == "grayscale":
    stops = [0.00, 0.34, 0.61, 0.84, 1.00]
    red   = [1.00, 0.84, 0.61, 0.34, 0.00]
    green = [1.00, 0.84, 0.61, 0.34, 0.00]
    blue  = [1.00, 0.84, 0.61, 0.34, 0.00]
    # elif name == "whatever":
    # (define more palettes)
  if name == "DeepSea":
    ncontours = 32
    stops = [0.00, 0.34, 0.61, 0.84, 1.00]
    red   = [0.00, 0.09, 0.18, 0.09, 0.00]
    green = [0.01, 0.02, 0.39, 0.68, 0.97]
    blue  = [0.17, 0.39, 0.62, 0.79, 0.97]
  if name == "DarkBodyRadiator":
    ncontours = 32
    stops = [0.00, 0.25, 0.50, 0.75, 1.00]
    red   = [0.00, 0.50, 1.00, 1.00, 1.00]
    green = [0.00, 0.00, 0.55, 1.00, 1.00]
    blue  = [0.00, 0.00, 0.00, 0.00, 1.00]
  if name == "BlueYellow":
    ncontours = 64
    stops = [0.00, 0.50, 1.00]
    red   = [0.00, 0.50, 1.00]
    green = [0.00, 0.50, 1.00]
    blue  = [0.50, 0.50, 0.00]
  if name == "Green":
    ncontours = 64
    stops = [0.00, 0.50, 1.00]
    red   = [0.00, 0.00, 0.00]
    green = [0.50, 0.50, 0.50]
    blue  = [0.00, 0.00, 0.00]
  if name == "Red":
    ncontours = 64
    stops = [0.00, 0.50, 1.00]
    red   = [0.50, 0.50, 0.50]
    green = [0.00, 0.00, 0.00]
    blue  = [0.00, 0.00, 0.00]
  if name == "RainBow":
    ncontours = 64
    stops = [0.00, 0.34, 0.61, 0.84, 1.00]
    red   = [0.00, 0.00, 0.87, 1.00, 0.51]
    green = [0.00, 0.81, 1.00, 0.20, 0.00]
    blue  = [0.51, 1.00, 0.12, 0.00, 0.00]
  else:
    # default palette, looks cool
    stops = [0.00, 0.34, 0.61, 0.84, 1.00]
    red   = [0.00, 0.00, 0.87, 1.00, 0.51]
    green = [0.00, 0.81, 1.00, 0.20, 0.00]
    blue  = [0.51, 1.00, 0.12, 0.00, 0.00]

  s = array('d', stops)
  r = array('d', red)
  g = array('d', green)
  b = array('d', blue)

  npoints = len(s)
  TColor.CreateGradientColorTable(npoints, s, r, g, b, ncontours)

  # For older ROOT versions
  #gStyle.CreateGradientColorTable(npoints, s, r, g, b, ncontours)
  gStyle.SetNumberContours(ncontours)
