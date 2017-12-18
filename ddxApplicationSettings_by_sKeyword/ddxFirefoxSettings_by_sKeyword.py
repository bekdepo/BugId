import os;
from dxConfig import dxConfig;
from fsFirstExistingFile import fsFirstExistingFile;
from mFileSystem import mFileSystem;
sProgramFilesPath_x86 = os.getenv("ProgramFiles(x86)") or os.getenv("ProgramFiles");
sProgramFilesPath_x64 = os.getenv("ProgramW6432");

dxConfigSettings = {
  # Settings used by all browsers (these should eventually be fine-tuned for each browser)
  "bApplicationTerminatesWithMainProcess": True,
  "nExcessiveCPUUsageCheckInitialTimeout": 30.0, # Give browser some time to load repro
  "cBugId.nExcessiveCPUUsageCheckInterval": 30.0, # Browser may be busy for a bit, but no longer than 30 seconds.
  "cBugId.nExcessiveCPUUsagePercent": 95,      # Browser msust be very, very busy.
  "cBugId.nExcessiveCPUUsageWormRunTime": 0.5, # Any well written function should return within half a second IMHO.
};

# Firefox stable (if installed, otherwise use Firefox Developer Edition if installed).
sFirefoxPath_x64 = sProgramFilesPath_x64 and fsFirstExistingFile(
  r"%s\Mozilla Firefox\firefox.exe" % sProgramFilesPath_x64,
);
sFirefoxPath_x86 = fsFirstExistingFile(
  r"%s\Mozilla Firefox\firefox.exe" % sProgramFilesPath_x86,
);
sFirefoxPath = sFirefoxPath_x64 or sFirefoxPath_x86;

sFirefoxProfilePath = mFileSystem.fsPath(os.getenv("TEMP"), "Firefox-profile");

def fasGetFirefoxStaticArguments(bForHelp):
  if bForHelp:
    # The folder may not exist at this point, so we cannot guarantee a 8.3 path
    # exists. Also, the 8.3 path may not be easily readable. Therefore, we'll
    # always use the long path in the help.
    sUsedFirefoxProfilePath = sFirefoxProfilePath;
  else:
    # Firefox cannot handle long paths (starting with "\\?\") so we'll use the
    # 8.3 path to make sure it will work. To get an 8.3 path, there should be a
    # file or folder for that path. In this case, we want a folder, so we'll
    # make sure it's created if it does not exist yet.
    if not mFileSystem.fbIsFolder(sFirefoxProfilePath):
      assert mFileSystem.fbCreateFolder(sFirefoxProfilePath), \
          "Cannot create Firefox profile folder %s" % sFirefoxProfilePath;
    sUsedFirefoxProfilePath = mFileSystem.fs83Path(sFirefoxProfilePath)
  return [
    "--no-remote",
    "-profile",
        sUsedFirefoxProfilePath,
  ];

def fasGetFirefoxOptionalArguments(bForHelp = False):
  return bForHelp and ["<dxConfig.sDefaultBrowserTestURL>"] or [dxConfig["sDefaultBrowserTestURL"]];

def fFirefoxCleanup():
  if mFileSystem.fbIsFolder(sFirefoxProfilePath):
    mFileSystem.fbDeleteChildrenFromFolder(sFirefoxProfilePath);
  else:
    assert mFileSystem.fbCreateFolder(sFirefoxProfilePath), \
        "Cannot create Firefox profile folder %s" % sFirefoxProfilePath;


# Known applications can have regular expressions that map source file paths in its output to URLs, so the details HTML for any detected bug can have clickable
# links to an online source repository:
srMozillaCentralSourceURLMappings = "".join([
  r"c:[\\/]builds[\\/]moz2_slave[\\/][^\\/]+[\\/]build[\\/](?:src[\\/])?", # absolute file path
  r"(?P<path>[^:]+\.\w+)", # relative file path
  r"(:| @ |, line )", # separator
  r"(?P<lineno>\d+)",  # line number
]);
dsURLTemplate_by_srSourceFilePath = {srMozillaCentralSourceURLMappings: "https://dxr.mozilla.org/mozilla-central/source/%(path)s#%(lineno)s"};

ddxFirefoxSettings_by_sKeyword = {
  "firefox": {
    "sBinaryPath": sFirefoxPath,
    "fasGetStaticArguments": fasGetFirefoxStaticArguments,
    "fasGetOptionalArguments": fasGetFirefoxOptionalArguments,
    "dxConfigSettings": dxConfigSettings,
    "fCleanup": fFirefoxCleanup,
    "dsURLTemplate_by_srSourceFilePath": dsURLTemplate_by_srSourceFilePath,
  },
  "firefox_x86": {
    "sBinaryPath": sFirefoxPath_x86,
    "fasGetStaticArguments": fasGetFirefoxStaticArguments,
    "fasGetOptionalArguments": fasGetFirefoxOptionalArguments,
    "dxConfigSettings": dxConfigSettings,
    "fCleanup": fFirefoxCleanup,
    "sISA": "x86",
    "dsURLTemplate_by_srSourceFilePath": dsURLTemplate_by_srSourceFilePath,
  },
  "firefox_x64": {
    "sBinaryPath": sFirefoxPath_x64,
    "fasGetStaticArguments": fasGetFirefoxStaticArguments,
    "fasGetOptionalArguments": fasGetFirefoxOptionalArguments,
    "dxConfigSettings": dxConfigSettings,
    "fCleanup": fFirefoxCleanup,
    "sISA": "x64",
    "dsURLTemplate_by_srSourceFilePath": dsURLTemplate_by_srSourceFilePath,
  },
};
