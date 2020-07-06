function versionDropdown() {
  const navTitles = document.getElementsByClassName("nav-item-0");
  const dropdown = createDropdown();
  for (let item of navTitles) {
    let newTitle = document.createElement("div");
    newTitle.appendChild(document.createTextNode("C-PAC "));
    newTitle.appendChild(dropdown);
    newTitle.appendChild(document.createTextNode(" documentation"));
    console.log(newTitle.innerHTML);
    item.innerHTML = newTitle.innerHTML;
  }
}

function createDropdown() {
    const here = window.location.href;
    const versionPattern = /(?<=.*fcp-indi\.github\..*\/docs\/)(.*)(?=\/.*)/;
    // ↓ temporary ↓
    const versions = ['latest', 'v1.6.2', 'develop'];
    // ↑ temporary ↑
    let dropdownElement = document.createElement('select');
    versions.forEach((version, i) => {
      let option = document.createElement('option');
      option.text = version;
      option.value = version;
      dropdownElement.add(option);
      let indexInString = here.search(versionPattern);
      if (indexInString !== -1) {
        dropdownElement.selectedIndex = i;
        // here.slice(indexInString, -1).split('/')[0];
      }
    });
    return(dropdownElement);
}