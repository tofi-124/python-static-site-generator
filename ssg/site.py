from pathlib import Path

class Site:
  def __init__(self,source, dest):
    self.source = Path(self.source)
    self.dest = Path(self.dest)

