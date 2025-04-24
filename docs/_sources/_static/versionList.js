const versionPattern = /(?<=.*fcp-indi\.github\..*\/docs\/)(.*)(?=\/.*)/;

function fetchValidVersions() {
  return fetch("https://fcp-indi.github.io/docs/versions.txt")
    .then(response => response.text())
    .then(version_list => version_list.split('\n').filter(v => v.trim() !== ''));
}

function validateDomain(here, selectedLocation) {
  const currentDomain = new URL(here).origin;
  const newDomain = new URL(selectedLocation).origin;
  if (currentDomain !== newDomain) {
    console.error("Redirect URL is not in the same domain:", selectedLocation);
    return false;
  }
  return true;
}


function validateAndRedirect(here, version) {
  fetchValidVersions().then(validVersions => {
    // Construct the redirect URL
    const indexInString = here.search(versionPattern);
    let suffix = here.slice(indexInString, here.length).split('\/');
    suffix = '/' + suffix.slice(1, suffix.length).join('\/');
    const selectedVersion = here.slice(0, indexInString) + version;
    const selectedLocation = selectedVersion + suffix;

    // Validate the version parameter
    if (!validVersions.includes(version)) {
      console.error("Invalid version selected:", version);
      return; // Do not proceed with the redirect
    }

    if ((selectedLocation !== here) && validateDomain(here, selectedLocation)) {
      const redirectURL = new URL(selectedLocation);
      // Perform the redirect if the URL is different and version is valid
      window.location.replace(redirectURL);
    }
  });
}

function createDropdown(here) {
  let promisedDropdown = function(resolve, reject) {
    fetchValidVersions().then(versions => {
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
      resolve(dropdownElement);
    });
  }
  return new Promise(promisedDropdown);
}

function versionDropdown() {
  const here = window.location.href;
  const dochome = new URL("https://" + here.split('/').slice(2, 5).join('/'));
  if (validateDomain(here, dochome)) {
    const navTitles = document.querySelectorAll(".brand,.sidebar-brand-text");
    createDropdown(here).then(dropdown => {
      for (let item of navTitles) {
        item.parentElement.removeAttribute("href");
        let newTitle = document.createElement("div");
        let newTitlePrefix = document.createElement("a");
        if (dochome.origin === window.location.origin) {
          newTitlePrefix.setAttribute("href", dochome);
        }
        newTitlePrefix.appendChild(document.createTextNode("C-PAC "));
        newTitle.appendChild(newTitlePrefix);
        newTitle.appendChild(dropdown);
        let newTitleSuffix = document.createElement("a");
        if (dochome.origin === window.location.origin) {
          newTitleSuffix.setAttribute("href", dochome);
        }
        newTitleSuffix.appendChild(document.createTextNode(" documentation"));
        newTitle.appendChild(newTitleSuffix);
        newTitle.appendChild(document.createTextNode(" »"));
        item.innerHTML = newTitle.innerHTML;
        item.addEventListener('change', (event) => {
          validateAndRedirect(here, event.target.value);
        });
      }
    });
  }
}

versionDropdown();
