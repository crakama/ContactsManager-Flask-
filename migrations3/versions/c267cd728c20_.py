"""empty message

Revision ID: c267cd728c20
Revises: None
Create Date: 2016-02-26 11:14:06.503000

"""

# revision identifiers, used by Alembic.
revision = 'c267cd728c20'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usercontacts', sa.Column('country', sa.String(length=140), nullable=True))
    op.add_column('usercontacts', sa.Column('email', sa.String(length=140), nullable=True))
    op.add_column('usercontacts', sa.Column('firstname', sa.String(length=140), nullable=True))
    op.add_column('usercontacts', sa.Column('lastname', sa.String(length=140), nullable=True))
    op.add_column('usercontacts', sa.Column('mobilenumber', sa.String(length=140), nullable=True))
    op.add_column('usercontacts', sa.Column('organization', sa.String(length=140), nullable=True))
    op.add_column('usercontacts', sa.Column('position', sa.String(length=140), nullable=True))
    op.alter_column('usercontacts', 'skypeID',
               existing_type=sa.VARCHAR(length=140),
               nullable=True)
    op.drop_column('usercontacts', 'Organization')
    op.drop_column('usercontacts', 'MobileNo')
    op.drop_column('usercontacts', 'Name')
    op.drop_column('usercontacts', 'Position')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usercontacts', sa.Column('Position', sa.VARCHAR(length=140), nullable=False))
    op.add_column('usercontacts', sa.Column('Name', sa.VARCHAR(length=140), nullable=False))
    op.add_column('usercontacts', sa.Column('MobileNo', sa.INTEGER(), nullable=False))
    op.add_column('usercontacts', sa.Column('Organization', sa.VARCHAR(length=140), nullable=False))
    op.alter_column('usercontacts', 'skypeID',
               existing_type=sa.VARCHAR(length=140),
               nullable=False)
    op.drop_column('usercontacts', 'position')
    op.drop_column('usercontacts', 'organization')
    op.drop_column('usercontacts', 'mobilenumber')
    op.drop_column('usercontacts', 'lastname')
    op.drop_column('usercontacts', 'firstname')
    op.drop_column('usercontacts', 'email')
    op.drop_column('usercontacts', 'country')
    ### end Alembic commands ###
