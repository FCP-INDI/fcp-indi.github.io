const versionPattern = /(?<=.*fcp-indi\.github\..*\/docs\/)(.*)(?=\/.*)/;

function versionDropdown() {
  const here = window.location.href;
  const dochome = "https://" + here.split('/').slice(2, 6).join('/'); // make this 5 for top-level domain
  const navTitles = document.getElementsByClassName("nav-item-0");
  const dropdown = createDropdown(here);
  for (let item of navTitles) {
    let newTitle = document.createElement("div");
    let newTitlePrefix = document.createElement("a");
    newTitlePrefix.setAttribute("href", dochome);
    console.log(newTitle);
    newTitlePrefix.appendChild(document.createTextNode("C-PAC "));
    newTitle.appendChild(newTitlePrefix);
    console.log(newTitle);
    newTitle.appendChild(dropdown);
    console.log(newTitle);
    let newTitleSuffix = document.createElement("a");
    newTitleSuffix.setAttribute("href", dochome);
    newTitleSuffix.appendChild(document.createTextNode(" documentation"));
    newTitle.appendChild(newTitleSuffix);
    newTitle.appendChild(document.createTextNode(" »"));
    console.log(newTitle);
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
  fetch("https://fcp-indi.github.io/docs/versions.txt").then(response => response.text().then(version_list => {
    const versions = version_list.split('\n');
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
  }));
}

versionDropdown();