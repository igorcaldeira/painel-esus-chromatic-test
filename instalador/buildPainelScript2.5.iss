; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "Painel Esus"
#define MyAppVersion "2.4"
#define MyAppPublisher "Fiocruz"
#define MyAppURL "https://painelsaude.fiocruz.br"
#define MyAppExeName "painel-esus.exe"
#define MyAppAssocName MyAppName + ""
#define MyAppAssocExt ".myp"
#define MyAppAssocKey StringChange(MyAppAssocName, " ", "") + MyAppAssocExt
#define ConfigExeName "config.exe"
#define rootPath "D:\a\painel-esus\painel-esus"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{91B895F7-3F8C-4B4C-A898-AF39516ADBFC}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName=C:\Fiocruz\{#MyAppName}
ChangesAssociations=yes
DisableProgramGroupPage=yes
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
OutputDir={#rootPath}\instalador\output
OutputBaseFilename=painel-esus-setup2.3
SetupIconFile={#rootPath}\painel-esus\icon\Icon_Painel_Purple_ICO.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "brazilianportuguese"; MessagesFile: "compiler:Languages\BrazilianPortuguese.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "{#rootPath}\painel-esus\dist\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#rootPath}\paineis-v2-front\static-files\*"; DestDir: "{app}\static-files"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "{#rootPath}\painel-esus\icon\*"; DestDir: "{app}\icon"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "{#rootPath}\painel-esus\dist\config.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#rootPath}\painel-esus\dist\painel-esus.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#rootPath}\painel-esus\ibge.csv"; DestDir: "{app}"; Flags: ignoreversion
;Source: "{#rootPath}\painel-esus\painel_esus.db"; DestDir: "{app}"; Flags: ignoreversion
;Source: "{#rootPath}\painel-esus\painel-esus.sqls"; DestDir: "{app}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Registry]
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocExt}\OpenWithProgids"; ValueType: string; ValueName: "{#MyAppAssocKey}"; ValueData: ""; Flags: uninsdeletevalue
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}"; ValueType: string; ValueName: ""; ValueData: "{#MyAppAssocName}"; Flags: uninsdeletekey
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\{#MyAppExeName},0"
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""
Root: HKA; Subkey: "Software\Classes\Applications\{#MyAppExeName}\SupportedTypes"; ValueType: string; ValueName: ".myp"; ValueData: ""

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#ConfigExeName}"; Description: "Abrir configuração após a instalação"; Flags: postinstall skipifsilent unchecked runascurrentuser; Check: ShouldRunExe
[Code]
function ShouldRunExe(): Boolean;
begin
  Result := WizardSilent() = False;  // Apenas rodar se o instalador não estiver no modo silencioso
end;
