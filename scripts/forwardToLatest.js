const oldPattern = /.*fcp-indi\.github\..*\/docs(\/user|\/developer|\/$|$)/;
const oldPatternDelim = /fcp-indi\.github\..*\/docs\//;
const notLatestPattern = /.*fcp-indi\.github\..*\/docs(?!\/latest|\/$|$)/;
const latestString = "/latest/";

function constructLatest(loc) {
  if (loc.search(oldPattern) !== -1) {
    const part0 = loc.match(oldPattern)[0].split('/').slice(0, -1).join('/');
    components = loc.split(oldPatternDelim);
    return(part0 + latestString + components[1]);
  } else if (loc.search(notLatestPattern) !== -1) {
    const part0 = loc.match(notLatestPattern)[0].split('/').slice(0, -1).join('/');
    components = loc.split(oldPatternDelim);
    return(part0 + latestString + components[1].split('/').slice(1,).join('/'));
  } else {
    return(loc);
  };
}

let latestURL = constructLatest(window.location.href);

if (latestURL !== window.location.href) {
  window.location.replace(latestURL);
}
