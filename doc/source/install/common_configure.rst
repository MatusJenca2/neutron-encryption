2. Edit the ``/etc/neutron-encryption/neutron-encryption.conf`` file and complete the following
   actions:

   * In the ``[database]`` section, configure database access:

     .. code-block:: ini

        [database]
        ...
        connection = mysql+pymysql://neutron-encryption:NEUTRON-ENCRYPTION_DBPASS@controller/neutron-encryption
