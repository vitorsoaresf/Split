"""fix: refactore patient_code to cpf

Revision ID: c13dcaca6f02
Revises: c80d30a58cba
Create Date: 2022-04-28 08:12:47.733305

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c13dcaca6f02'
down_revision = 'c80d30a58cba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('patients', sa.Column('cpf', sa.String(), nullable=True))
    op.add_column('patients', sa.Column('address_id', sa.Integer(), nullable=True))
    op.alter_column('patients', 'birth_date',
               existing_type=sa.DATE(),
               type_=sa.String(),
               existing_nullable=True)
    op.create_foreign_key(None, 'patients', 'address', ['address_id'], ['address_id'])
    op.drop_column('patients', 'patient_code')
    op.drop_column('patients', 'city')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('patients', sa.Column('city', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('patients', sa.Column('patient_code', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'patients', type_='foreignkey')
    op.alter_column('patients', 'birth_date',
               existing_type=sa.String(),
               type_=sa.DATE(),
               existing_nullable=True)
    op.drop_column('patients', 'address_id')
    op.drop_column('patients', 'cpf')
    # ### end Alembic commands ###
