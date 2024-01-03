sudo ln -s ${PWD}/configuration.nix /etc/nixos/configuration.nix

for config in *; do
	if [ -d config ]
	then
		sudo ln -s ${PWD}/${config}/* /etc/nixos/modules/${config}/
	fi
done
