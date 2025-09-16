$masterNodeName = "_k8s_master_masterklass"
$numMasterNode = 3

$workerNodeName = "_k8s_worke_masterklass"
$numWorkerNode = 2

$hvSwitchName = "MyLocalNet"
$osIso = "E:\ISO\ubuntu-22.04.2-live-server-amd64.iso"

$location_path_vm = "D:\VM"

for ($i=1; $i -le $numMasterNode; $i++)
{
	$Exists = get-vm -name $masterNodeName$i -ErrorAction SilentlyContinue
	if (-not $Exists)
	{
		New-VM -Name $masterNodeName$i -MemoryStartupBytes 2GB -BootDevice VHD -NewVHDPath $location_path_vm\$masterNodeName$i\$masterNodeName$i.vhdx -Path $location_path_vm -NewVHDSizeBytes 30GB -Generation 2 -Switch $hvSwitchName
		Set-VMProcessor $masterNodeName$i -Count 2
		Set-VMFirmware $masterNodeName$i -EnableSecureBoot Off
		Set-VM -Name $masterNodeName$i -CheckpointType Disabled
		Add-VMDvdDrive -VMName $masterNodeName$i -Path $osIso
		Set-VMFirmware -VMName $masterNodeName$i -BootOrder $(Get-VMDvdDrive -VMName $masterNodeName$i), $(Get-VMHardDiskDrive -VMName $masterNodeName$i)
		Set-VMNetworkAdapter -VMName $masterNodeName$i -StaticMacAddress "10000000000$i"
		Set-VMMemory -VMName $masterNodeName$i -DynamicMemoryEnabled $false
		Write-Host "THE VM $masterNodeName$i HAS BEEN CREATED."
	}
	else
    {
		Write-Host "THE VM $masterNodeName$i IS ALREADY EXIST."
	}
}


for ($z=1; $z -le $numWorkerNode; $z++)
{
	$Exists = get-vm -name $workerNodeName$z -ErrorAction SilentlyContinue
	if (-not $Exists)
	{
		New-VM -Name $workerNodeName$z -MemoryStartupBytes 6GB -BootDevice VHD -NewVHDPath $location_path_vm\$workerNodeName$z\$workerNodeName$z.vhdx -Path $location_path_vm -NewVHDSizeBytes 100GB -Generation 2 -Switch $hvSwitchName
		Copy-Item "data.vhdx" -Destination $location_path_vm\$workerNodeName$z
		Set-VMProcessor $workerNodeName$z -Count 4
		Set-VMFirmware $workerNodeName$z -EnableSecureBoot Off
		Set-VM -Name $workerNodeName$z -CheckpointType Disabled
		Add-VMHardDiskDrive -VMName $workerNodeName$z -ControllerType SCSI -Path $location_path_vm\$workerNodeName$z\data.vhdx
		Add-VMDvdDrive -VMName $workerNodeName$z -Path $osIso
		Set-VMFirmware -VMName $workerNodeName$z -BootOrder $(Get-VMDvdDrive -VMName $workerNodeName$z), $(Get-VMHardDiskDrive -VMName $workerNodeName$z)[0]
		Set-VMNetworkAdapter -VMName $workerNodeName$z -StaticMacAddress "10000000100$z"
		Set-VMMemory -VMName $workerNodeName$z -DynamicMemoryEnabled $false
		Write-Host "THE VM $workerNodeName$z HAS BEEN CREATED."
	}
	else
    {
		Write-Host "THE VM $workerNodeName$z IS ALREADY EXIST."
	}
}

$clientName = "_k8s_client_masterklass"

$Exists = get-vm -name _k8s_client_masterklass -ErrorAction SilentlyContinue
if (-not $Exists)
{
	New-VM -Name $clientName -MemoryStartupBytes 2GB -BootDevice VHD -NewVHDPath $location_path_vm\$clientName\$clientName.vhdx -Path $location_path_vm -NewVHDSizeBytes 80GB -Generation 2 -Switch $hvSwitchName
	Set-VMProcessor $clientName -Count 2
	Set-VMFirmware $clientName -EnableSecureBoot Off
	Set-VM -Name $clientName -CheckpointType Disabled
	Add-VMDvdDrive -VMName $clientName -Path $osIso
	Set-VMFirmware -VMName $clientName -BootOrder $(Get-VMDvdDrive -VMName $clientName), $(Get-VMHardDiskDrive -VMName $clientName)
	Set-VMNetworkAdapter -VMName $clientName -StaticMacAddress "100000000044"
	Set-VMMemory -VMName $clientName -DynamicMemoryEnabled $false
	Write-Host "THE VM $clientName HAS BEEN CREATED."
}
else
{
	Write-Host "THE VM $clientName IS ALREADY EXIST."
}

$Exists = get-vm -name postgresql -ErrorAction SilentlyContinue
if (-not $Exists)
{
	New-VM -Name postgresql -MemoryStartupBytes 2GB -BootDevice VHD -NewVHDPath $location_path_vm\postgresql\postgresql.vhdx -Path $location_path_vm -NewVHDSizeBytes 80GB -Generation 2 -Switch $hvSwitchName
	Set-VMProcessor postgresql -Count 2
	Set-VMFirmware postgresql -EnableSecureBoot Off
	Set-VM -Name postgresql -CheckpointType Disabled
	New-VHD -Path $location_path_vm\postgresql\data.vhdx -SizeBytes 40GB
	Add-VMHardDiskDrive -VMName postgresql -ControllerType SCSI -Path $location_path_vm\postgresql\data.vhdx
	Add-VMDvdDrive -VMName postgresql -Path $osIso
	Set-VMFirmware -VMName postgresql -BootOrder $(Get-VMDvdDrive -VMName postgresql), $(Get-VMHardDiskDrive -VMName postgresql)[0]
	Set-VMNetworkAdapter -VMName postgresql -StaticMacAddress "000000000045"
	Set-VMMemory -VMName postgresql -DynamicMemoryEnabled $false
	Write-Host "THE VM postgresql HAS BEEN CREATED."
}
else
{
	Write-Host "THE VM postgresql IS ALREADY EXIST."
}

$Exists = get-vm -name Nexus -ErrorAction SilentlyContinue
if (-not $Exists)
{
	New-VM -Name Nexus -MemoryStartupBytes 4GB -BootDevice VHD -NewVHDPath $location_path_vm\Nexus\Nexus.vhdx -Path $location_path_vm -NewVHDSizeBytes 30GB -Generation 2 -Switch $hvSwitchName
	New-VM -Name Nexus -MemoryStartupBytes 4GB -BootDevice VHD -NewVHDPath $location_path_vm\Nexus\Nexus.vhdx -Path $location_path_vm -NewVHDSizeBytes 30GB -Generation 2 -Switch $hvSwitchName
	Set-VMProcessor Nexus -Count 4
	Set-VMFirmware Nexus -EnableSecureBoot Off
	Set-VM -Name Nexus -CheckpointType Disabled
	New-VHD -Path $location_path_vm\Nexus\data.vhdx -SizeBytes 100GB
	Add-VMHardDiskDrive -VMName Nexus -ControllerType SCSI -Path $location_path_vm\Nexus\data.vhdx
	Add-VMDvdDrive -VMName Nexus -Path $osIso
	Set-VMFirmware -VMName Nexus -BootOrder $(Get-VMDvdDrive -VMName Nexus), $(Get-VMHardDiskDrive -VMName Nexus)[0]
	Set-VMNetworkAdapter -VMName Nexus -StaticMacAddress "000000000046"
	Set-VMMemory -VMName Nexus -DynamicMemoryEnabled $false
	Write-Host "THE VM Nexus HAS BEEN CREATED."
}
else
{
	Write-Host "THE VM Nexus IS ALREADY EXIST."
}

