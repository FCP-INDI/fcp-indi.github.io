const versionPattern = /(?<=.*fcp-indi\.github\..*\/docs\/)(.*)(?=\/.*)/;

function versionDropdown() {
  const here = window.location.href;
  const navTitles = document.getElementsByClassName("nav-item-0");
  const dropdown = createDropdown(here);
  for (let item of navTitles) {
    let newTitle = document.createElement("div");
    newTitle.appendChild(document.createTextNode("C-PAC "));
    newTitle.appendChild(dropdown);
    newTitle.appendChild(document.createTextNode(" documentation"));
    item.innerHTML = newTitle.innerHTML;
    item.addEventListener('change', (event) => {
      redirectVersion(here, event.target.value);
    });
  }
}


function redirectVersion(here, version) {
  const indexInString = here.search(versionPattern);
  let suffix = here.slice(indexInString, here.length).split('\/');
  suffix = '/' + suffix.slice(1,suffix.length).join('\/');
  const selectedLocation = here.slice(0, indexInString) + version + suffix;
  if (selectedLocation !== here) {
    window.location.replace(selectedLocation);
  }
}


function createDropdown(here) {
  // ↓ temporary ↓
  const versions = ['latest', 'v1.6.2a', 'develop'];
  // ↑ temporary ↑
  let dropdownElement = document.createElement('select');
  versions.forEach(version => {
    let option = document.createElement('option');
    option.text = version;
    option.value = version;
    dropdownElement.add(option);
    let indexInString = here.search(versionPattern);
    if (here.slice(indexInString, indexInString + version.length) === version) {
      option.setAttribute('selected', 'selected');
    }
  });
  return(dropdownElement);
}

versionDropdown();