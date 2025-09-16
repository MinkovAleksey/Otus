# Подготовка инфраструктуры из 3-ёх master nodes и 2 worker nodes
  Файлы для подготовки инфраструктуры(хостов)
  поддерживается:
## Hyper-V - powershell script \
   Переменные в скрипте:\
      $masterNodeName - маска для имени master nodes \
      $numMasterNode - число master nodes \
      $workerNodeName - маска для имени worker nodes \
      $numWorkerNode - число worker nodes \
      $hvSwitchName - имя виртуального switck к которому будет подключены хосты \
      $osIso - полный путь до ISO файло OS \
      $location_path_vm - путь где будут созданы VM

  Создаются виртуальные машины с заданными параметрами CPU/RAM/HDD/mac-address
  VM получают IP адреса по DHCP из заранее настроеного распределения mac -> ip 
