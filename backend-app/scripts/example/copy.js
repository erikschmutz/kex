const fs = require("fs");
const path = require("path");

const amount = Number.parseInt(process.argv[2]);
const newPath = process.argv[3];

console.log(`Copying ${amount} to new folder ${newPath}`);
const folders = fs.readdirSync("./data");

fs.mkdirSync(newPath);
console.log(`Successfully created new, ${newPath}✔️`);

let movedFolders = 0;

for (const folder of folders) {
  fs.mkdirSync(path.join(newPath, folder));

  movedFolders++;
  if (movedFolders >= amount) break;
}
console.log(`Successfully copied folders(${folders.length}) ✔️`);

movedFolders = 0;
let movedFiles = 0;
for (const folder of folders) {
  for (const file of fs.readdirSync(path.join("data", folder))) {
    fs.copyFileSync(
      path.join("data", folder, file),
      path.join(newPath, folder, file)
    );
    movedFiles++;
  }

  movedFolders++;
  if (movedFolders >= amount) break;
}

console.log(`Successfully copied files(${movedFiles}) ✔️`);
