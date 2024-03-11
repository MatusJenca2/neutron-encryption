NEUTRON_ENCRYPTION_XTRACE=$(set +o | grep xtrace)
set -o xtrace
function neutron_encryption_install {
    setup_develop /opt/stack/neutron-encryption
    echo "Installing Neutron encryption plugin" >> encryption-test.log
}

function neutron_encryption_configure {
    neutron_service_plugin_class_add encryption
    configure_l3_agent
    echo "Configuring Neutron encryption plugin" >> encryption-test.log
}


if [[ "$1" == "stack" && "$2" == "install" ]]; then
    neutron_encryption_install

elif [[ "$1" == "stack" && "$2" == "post-config" ]]; then
    neutron_encryption_configure
fi


$NEUTRON_ENCRYPTION_XTRACE