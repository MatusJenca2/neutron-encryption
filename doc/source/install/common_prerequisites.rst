Prerequisites
-------------

Before you install and configure the neutron-encryption service,
you must create a database, service credentials, and API endpoints.

#. To create the database, complete these steps:

   * Use the database access client to connect to the database
     server as the ``root`` user:

     .. code-block:: console

        $ mysql -u root -p

   * Create the ``neutron-encryption`` database:

     .. code-block:: none

        CREATE DATABASE neutron-encryption;

   * Grant proper access to the ``neutron-encryption`` database:

     .. code-block:: none

        GRANT ALL PRIVILEGES ON neutron-encryption.* TO 'neutron-encryption'@'localhost' \
          IDENTIFIED BY 'NEUTRON-ENCRYPTION_DBPASS';
        GRANT ALL PRIVILEGES ON neutron-encryption.* TO 'neutron-encryption'@'%' \
          IDENTIFIED BY 'NEUTRON-ENCRYPTION_DBPASS';

     Replace ``NEUTRON-ENCRYPTION_DBPASS`` with a suitable password.

   * Exit the database access client.

     .. code-block:: none

        exit;

#. Source the ``admin`` credentials to gain access to
   admin-only CLI commands:

   .. code-block:: console

      $ . admin-openrc

#. To create the service credentials, complete these steps:

   * Create the ``neutron-encryption`` user:

     .. code-block:: console

        $ openstack user create --domain default --password-prompt neutron-encryption

   * Add the ``admin`` role to the ``neutron-encryption`` user:

     .. code-block:: console

        $ openstack role add --project service --user neutron-encryption admin

   * Create the neutron-encryption service entities:

     .. code-block:: console

        $ openstack service create --name neutron-encryption --description "neutron-encryption" neutron-encryption

#. Create the neutron-encryption service API endpoints:

   .. code-block:: console

      $ openstack endpoint create --region RegionOne \
        neutron-encryption public http://controller:XXXX/vY/%\(tenant_id\)s
      $ openstack endpoint create --region RegionOne \
        neutron-encryption internal http://controller:XXXX/vY/%\(tenant_id\)s
      $ openstack endpoint create --region RegionOne \
        neutron-encryption admin http://controller:XXXX/vY/%\(tenant_id\)s
