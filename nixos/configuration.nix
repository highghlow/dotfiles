{ config, ... }:

{
	imports = [
		"./hardware-configuration.nix"
		"./modules/*.nix"
		"./modules/*/*.nix"
	]
}
