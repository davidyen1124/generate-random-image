import requests
from PIL import Image, ImageDraw

def getGrid():
  url = 'https://www.random.org/integers/?num=4096&min=0&max=255&col=64&base=10&format=plain&rnd=new'
  text = requests.get(url).text
  return [line.strip().split('\t') for line in text.strip().split('\n')]


def main():
  grids = [getGrid() for i in range(3)]

  img = Image.new('RGB', (64, 64), 'white')
  pen = ImageDraw.Draw(img)

  for i in range(64):
    for j in range(64):
      r = int(grids[0][i][j])
      g = int(grids[1][i][j])
      b = int(grids[2][i][j])
      pen.point((i, j), (r, g, b))

  img.save('output.png', 'png')

if __name__ == '__main__':
  main()
