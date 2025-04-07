import urllib.request, os

def getProviders():
  """
  Fetches the providers.tf file from the knifedrop GitHub repository.
  """
  # URL of the providers.tf file in the knifedrop GitHub repository
  url = 'https://raw.githubusercontent.com/michaelkemp/knifedrop/refs/heads/main/templates/providers.tf'
  response = urllib.request.urlopen(url)
  data = response.read()
  text = data.decode('utf-8')

  cwd = os.path.dirname(os.path.realpath(__file__))
  tfDir =  os.path.join(cwd, "terraform")
  if not os.path.exists(tfDir):
    os.makedirs(tfDir)
  print(tfDir)
  # Write the content to a file named providers.tf in the terraform directory
  with open(os.path.join(tfDir, 'providers.tf'), 'w') as f:
    f.write(text)
    f.close()
    print("written")

if __name__ == "__main__":
  getProviders()
  print("done")